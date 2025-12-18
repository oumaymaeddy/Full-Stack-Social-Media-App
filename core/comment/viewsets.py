from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.comment.serializers import CommentSerializer
from core.auth.permissions import UserPermission
from core.post.models import Post


class CommentViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()

        post_pk = self.kwargs.get('post_pk')
        if post_pk is None:
            raise Http404("Post ID not provided")

        return Comment.objects.filter(post__public_id=post_pk)

    def get_object(self):
        obj = get_object_or_404(Comment, public_id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        post_pk = kwargs.get('post_pk')
        post = get_object_or_404(Post, public_id=post_pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Lier l'auteur et le post
        serializer.save(author=request.user, post=post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
