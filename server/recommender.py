import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords 
from nltk.tokenize import WordPunctTokenizer
import warnings
import string
import nltk
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')


def recommend(request):
    print(request)
    df = pd.read_csv('data/out.csv')
    df_business = pd.read_csv('data/places.csv')

    #Select only stars and text
    #replaced 'business_id', 'user_id', 'stars', 'text' with 
    bus_data = df[['gPlusPlaceId', 'gPlusUserId', 'rating', 'reviewText']]
    stop = []
    for word in stopwords.words('english'):
        s = [char for char in word if char not in string.punctuation]
        stop.append(''.join(s))


    def text_process(mess):
        """
        Takes in a string of text, then performs the following:
        1. Remove all punctuation
        2. Remove all stopwords
        3. Returns a list of the cleaned text
        """
        # Check characters to see if they are in punctuation
        if(isinstance(mess, float)):
            return " "
        else:
            nopunc = [char for char in mess if char not in string.punctuation]
        # Join the characters again to form the string.
            nopunc = ''.join(nopunc)
            
            # Now just remove any stopwords
            return " ".join([word for word in nopunc.split() if word.lower() not in stop])


    bus_data['reviewText'] = bus_data['reviewText'].apply(text_process)

    userid_df = bus_data[['gPlusUserId','reviewText']]
    business_df = bus_data[['gPlusPlaceId', 'reviewText']]

    from sklearn.feature_extraction.text import TfidfVectorizer
    #userid vectorizer
    userid_vectorizer = TfidfVectorizer(tokenizer = WordPunctTokenizer().tokenize, max_features=400)
    userid_vectors = userid_vectorizer.fit_transform(userid_df['reviewText'])
    #Business id vectorizer
    businessid_vectorizer = TfidfVectorizer(tokenizer = WordPunctTokenizer().tokenize, max_features=400)
    businessid_vectors = businessid_vectorizer.fit_transform(business_df['reviewText'])

    # userid_rating_matrix = pd.pivot_table(bus_data, values='rating', index=['gPlusUserId'], columns=['gPlusPlaceId'])

    # def matrix_factorization(R, P, Q, steps=25, gamma=0.001,lamda=0.02):
    #     print(R)
    #     for step in range(steps):
    #         for i in R.index:
    #             for j in R.columns:
    #                 if R.loc[i,j]>0:
    #                     print(i, j)
    #                     print(P.loc[i])
    #                     print(Q.loc[j])
    #                     print("HIHIHIHIHHIHIHI")
    #                     print(P.loc[i].transpose())
    #                     eij=R.loc[i,j]-np.dot(Q.loc[j],P.loc[i].transpose())
    #                     P.loc[i]=P.loc[i]+gamma*(eij*Q.loc[j]-lamda*P.loc[i])
    #                     Q.loc[j]=Q.loc[j]+gamma*(eij*P.loc[i]-lamda*Q.loc[j])
    #         e=0
    #         for i in R.index:
    #             for j in R.columns:
    #                 if R.loc[i,j]>0:
    #                     e= e + pow(R.loc[i,j]-np.dot(P.loc[i],Q.loc[j]),2)+lamda*(pow(np.linalg.norm(P.loc[i]),2)+pow(np.linalg.norm(Q.loc[j]),2))
    #         if e<0.001:
    #             break
            
    #     return P,Q

    P = pd.DataFrame(userid_vectors.toarray(), index=userid_df.gPlusUserId, columns=userid_vectorizer.get_feature_names())
    Q = pd.DataFrame(businessid_vectors.toarray(), index=business_df.gPlusPlaceId, columns=businessid_vectorizer.get_feature_names())
    # print(P)
    # print(Q.head())
    # P, Q = matrix_factorization(userid_rating_matrix, P, Q, steps=25, gamma=0.001,lamda=0.02)

    # Store P, Q and vectorizer in pickle file
    import pickle
    output = open('FindMyRestaurant.pkl', 'wb')
    pickle.dump(P,output)
    pickle.dump(Q,output)
    pickle.dump(userid_vectorizer,output)
    output.close()



    words = request
    test_df= pd.DataFrame([words], columns=['reviewText'])
    test_df['reviewText'] = test_df['reviewText'].apply(text_process)
    test_vectors = userid_vectorizer.transform(test_df['reviewText'])
    test_v_df = pd.DataFrame(test_vectors.toarray(), index=test_df.index, columns=userid_vectorizer.get_feature_names())

    predictItemRating=pd.DataFrame(np.dot(test_v_df.loc[0],Q.T),index=Q.index,columns=['Rating'])
    topRecommendations=pd.DataFrame.sort_values(predictItemRating,['Rating'],ascending=[0])[:5]

    dict_arr = []
    for i in topRecommendations.index:
        rect_dict = {}
        rect_dict['name'] = df_business[df_business['gPlusPlaceId']==i]['name'].iloc[0]
        # rect_dict['categories'] = df[df['gPlusPlaceId']==i]['categories'].iloc[0]
        rect_dict['rating'] = str(df[df['gPlusPlaceId']==i]['rating'].iloc[0])
        rect_dict['gPlusPlaceId'] = i
        rect_dict['address'] = df_business[df_business['gPlusPlaceId']==i]['address'].iloc[0]
        dict_arr.append(rect_dict)
    
    return dict_arr