from scikit import tree

#[height,weight,shoe size]
X=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]

Y=['male','female','female','female','male','male','male','female','male','female','male']

#clf (short for classifier) variable to store decision tree model or classifier
clf=tree.DecisionTreeClassifier()

clf=clf.fit(X,Y)

#we use the variable: prediction to store the result of the new values which are compared to our tree values to predict the gender
prediction=clf.predict([[190,70,43]])
print(prediction)