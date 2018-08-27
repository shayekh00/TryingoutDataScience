from sklearn import tree

X=[ [181,80,44],[177,70,43],[181,80,44],[181,80,44],[181,80,44],[181,80,44],[181,80,44],[181,80,44],[181,80,44],[181,80,44],[181,80,44]]

Y= ['male','female','female','male' ,'female','male','female','female','male' ,'female','male']

clf=tree.DecisionTreeClassifier()

clf=clf.fit(X,Y)

prediction=clf.predict([[190,70,42]])

print (prediction)

#sgafsaf