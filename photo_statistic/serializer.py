from rest_framework import serializers
from photo_statistic.models import PhotoStatistic
from photo.models import Photo
from photo.serializer import PhotoSerializer
from nltk import tokenize
from operator import itemgetter
import math
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

class PhotoStatisticSerializer(serializers.ModelSerializer):
    statistic = serializers.SerializerMethodField()
    # photo_description = serializers.SerializerMethodField()

    class Meta:
        model = PhotoStatistic
        fields = ('statistic','photo_statistic_id')        

    def get_statistic(self, statistic):
        item = statistic.photo.__dict__
        stop_words = set(stopwords.words('portuguese'))
        words = item['photo_description']
        total_words = words.split()
        total_word_length = len(total_words)
        total_sentences = tokenize.sent_tokenize(words)
        total_sent_len = len(total_sentences)
            
        tf_score = {}
        for each_word in total_words:
            each_word = each_word.replace('.','')
            if each_word not in stop_words:
                if len(each_word) > 2:
                    if each_word in tf_score:
                        tf_score[each_word] += 1
                    else:
                        tf_score[each_word] = 1
            
        tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())
        photos = Photo.objects.all()
        
        return tf_score
    