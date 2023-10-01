from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics




class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
        
    
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    
    
    
    

# class ReviewDatail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    # queryset = Review.objects.all()
    # serializer_class = ReviewSerializer
    
    # def get(self, request, *args, **kwargs):
        # return self.retrieve(request, *args, **kwargs)
    

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # queryset = Review.objects.all()
    # serializer_class = ReviewSerializer

    # def get(self, request, *args, **kwargs):
        # return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
        # return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class WatchListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailAV(APIView):
    
        def get(self, request, pk):
            try:
                platform = StreamPlatform.objects.get(pk=pk)
            except StreamPlatform.DoesNotExist:
                return Response({'Error': "Doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
            serializer = StreamPlatformSerializer(platform, context={'request': request})
            return Response(serializer.data)
        
        def put(self, request, pk):
            movie =  StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        def delete(self, request, pk):
            movie =  StreamPlatform.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        
        
        
class WatchDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            movie =  WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': "Doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchSerializer(movie)
        return Response(serializer.data)
        
    def put(self, request, pk):
        movie =  WatchList.objects.get(pk=pk)
        serializer = WatchSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
    def delete(self, request, pk):
        movie =  WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



























        
        

# @ api_view(['GET', 'POST'])
# def movie_list(request):
    # if request.method == 'GET':
        # movie = Movie.objects.all()
        # serializer = MovieSerializer(movie, many=True)
        # return Response(serializer.data)

    # if request.method == 'POST':
        # serializer = MovieSerializer(data=request.data)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
        # else:
            # return Response(serializer.errors)
        
        
        
# @ api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
    # if request.method == 'GET':
        
        # try:
            # movie =  Movie.objects.get(pk=pk)
        # except Movie.DoesNotExist:
            # return Response({'Error': "Movie doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        # serializer = MovieSerializer(movie)
        # return Response(serializer.data)

    # if request.method == 'PUT':
        # movie =  Movie.objects.get(pk=pk)
        # serializer = MovieSerializer(movie, data=request.data)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
        # else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # if request.method == 'DELETE':
        # movie =  Movie.objects.get(pk=pk)
        # movie.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)