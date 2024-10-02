from rest_framework import serializers

from api.models import Book,Review

        
class ReviewSerializer(serializers.ModelSerializer):
    
    book_object=serializers.StringRelatedField()
    
    class Meta:
        
        model=Review
        
        fields= "__all__"
        
        read_only_fields=["id","book_object"]
        
        
class BookSerializer(serializers.ModelSerializer):
    
    # reviews=ReviewSerializer(read_only=True,many=True)
    
    reviews=serializers.SerializerMethodField(read_only=True)

    
    # review_count=serializers.CharField(read_only=True)
    
    review_count=serializers.SerializerMethodField(read_only=True)
    
    # avg_rating=serializers.IntegerField(read_only=True)
    
    avg_rating=serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        
        model=Book
        
        fields=["id","title","author","language","genre","price","review_count","avg_rating","reviews"]
        
        
    def get_review_count(self,obj):
        
        return Review.objects.filter(book_object=obj).count()
    
    def avg_rating(self,obj):
        
        reviews=Review.objects.filter(book_object=obj)
        
        avg=0
        
        if reviews:
            
            avg=sum([r.rating  for r in reviews])/reviews.count()
        
        return avg
    
    
    def get_reviews(self,obj):
        
        qs=Review.objects.filter(book_object=obj)
        
        serializer_instance=ReviewSerializer(qs,many=True)
        
        return serializer_instance.data