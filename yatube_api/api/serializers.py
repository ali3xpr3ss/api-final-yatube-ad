from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ['id', 'author', 'text', 'created', 'post']
        read_only_fields = ['id', 'created', 'post']
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    def validate(self, data):
        if 'following' not in data:
            raise serializers.ValidationError(
                {'following': 'Обязательное поле.'}
            )
        return data

    def validate_following(self, value):
        request = self.context.get('request')

        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("Требуется авторизация")

        if request.user == value:
            raise serializers.ValidationError("Нельзя подписаться "
                                              "на самого себя!")

        if Follow.objects.filter(user=request.user, following=value).exists():
            raise serializers.ValidationError("Вы уже подписаны "
                                              "на этого пользователя")

        return value

    class Meta:
        fields = '__all__'
        model = Follow
