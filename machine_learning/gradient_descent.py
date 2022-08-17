import numpy as np 
def best_fit(x,y):
    m_curr=b_curr=0
    n=len(x)
    iteration=10000
    learning_rate=0.08
    for i in range(iteration):
        y_predict=m_curr*x+b_curr
        md=-(2/n)*sum(x*(y-y_predict))
        bd=-(2/n)*sum(y-y_predict)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print("m {},b {},iteration {}".format(m_curr,b_curr,i))
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])
best_fit(x,y)