from sklearn import preprocessing,cross_validation, neighbors

class solar_power_prediction_model:
    X1 = np.array(df_test['cloudCover'][192:215])
    X2 = np.array(df_test['cloudCover'][216:239])
    X1 = X1.reshape(len(X1),-1)
    X2 = X2.reshape(len(X2),-1)

    y1 = np.array(df_test['powerProduction'][192:215])
    y2 = np.array(df_test['powerProduction'][216:239])

    accuracy1=[]
    accuracy2=[]


    from sklearn.model_selection import train_test_split
    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2,random_state=42 )
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2,random_state=42 )


    from sklearn.linear_model import SGDRegressor
    clf1 = SGDRegressor()
    clf1.fit(X1_train,y1_train)
    y1_rbf = clf1.predict(X1_test)

    from sklearn.metrics import mean_absolute_error
    print(mean_absolute_error(y1_test, y1_rbf))


    from sklearn.linear_model import SGDRegressor
    clf2 = SGDRegressor()
    clf2.fit(X2_train,y2_train)
    y2_rbf = clf2.predict(X2_test)
    print(mean_absolute_error(y2_test, y2_rbf))

# for i in range(100):

    X1_train,X1_test,y1_train,y1_test = cross_validation.train_test_split(X1,y1,test_size=0.3)
    X2_train,X2_test,y2_train,y2_test = cross_validation.train_test_split(X2,y2,test_size=0.3)
    clf3 =neighbors.KNeighborsClassifier()
    clf4 =neighbors.KNeighborsClassifier()
    clf3.fit(X1_train,y1_train)
    clf4.fit(X2_train,y2_train)
    accuracy1.append(clf3.score(X1_test,y1_test))
    accuracy2.append(clf4.score(X2_test,y2_test))

    plt.plot(accuracy1,'r',label="Day 1")
    plt.plot(accuracy1,'r',label="Day 2")

    plt.xlabel('Number of repetations')
    plt.ylabel('Accuracy')
    plt.title('Range of Accuracy for KNN Method')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
