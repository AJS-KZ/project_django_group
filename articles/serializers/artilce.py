from rest_framework import serializers

from articles.models import Article, ArticleFile


class ArticleFileAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleFile,
        fields = '__all__'


class ArticleFileForArticleListSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = ArticleFile,
        fields = ('file', )


class ArticleAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField('get_files')

    def get_files(self, instance):
        if instance.files is not None:
            files = instance.files.all()
            res = [ArticleFileAllSerializer(files, many=True).data]
            for file in files:
                res.append(ArticleFileAllSerializer(file).data)
            return res
        else:
            return []

    class Meta:
        model = Article
        fields = 'title', 'type', 'files'


class ArticleCreateSerializer(serializers.Serializer):
    class Meta:
        fields = 'title', 'type', 'files_ids'

    def validate(self, attrs):
        title = attrs.get('title') or None
        type = attrs.get('type') or None
        files_ids = attrs.get('files_ids') or None


        return attrs

    def create(self, validated_data):
        files_ids = validated_data.pop('files_ids')
        instance = super().save(validated_data)
        return instance