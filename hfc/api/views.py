
# import pandas as pd
# import operator
# from collections import OrderedDict



# meal_items = pd.read_pickle(r'\meal_items_2.pickle')

# k = 2
# c = [640-k,640+k]
# m = {}
# for i in meal_items:
#     if meal_items[i][0] in range(640-k,640+k):
#         m[meal_items[i]] = i

# sorted_tuples = sorted(m.values(), key=operator.itemgetter(1))
# m[sorted_tuples]


from hnfc.meal import MealPlanner

from rest_framework.generics import GenericAPIView
from .serializers import CaloriesSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class RecommendFoodView(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = CaloriesSerializer
    
    
    # def login(self):
    #     self.user = self.serializer.validated_data['user']
    #     self.token, _ = TokenModel.objects.get_or_create(user=self.user)


    def get_response(self):
        # serializer_class = TokenSerializer

        # serializer = serializer_class(instance=self.token, context={'request': self.request})

        response = Response(MealPlanner(self.CALORIES).meals())
        
        return response


    def post(self, request, *args, **kwargs):
        self.request = request
        
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})

        self.serializer.is_valid(raise_exception=True)
        self.CALORIES = self.serializer.data['calories']
        # self.login()
        return self.get_response()