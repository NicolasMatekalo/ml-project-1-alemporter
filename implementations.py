def least_squares_GD(y, tx, initial_w, max_iters, gamma):
    ''' Linear regression using gradient descent.
    
    Args:
        y: numpy array of shape (N,), N is the number of samples.
        tx: numpy array of shape (N,D), D is the number of features.
        initial_w: numpy array of shape=(2, ). The initial guess (or the initialization) for the model parameters
        max_iters: a scalar denoting the total number of iterations of GD
        gamma: a scalar denoting the stepsize

    Returns:
        w: optimal weights, numpy array of shape(D,), D is the number of features.
        loss: scalar denoting the loss value of the least squares

    >>> least_squares(np.array([0.1,0.2]), np.array([[2.3, 3.2], [1., 0.1]]))
    (array([ 0.21212121, -0.12121212]), 8.666684749742561e-33)
    '''
  return
def least_squares_SGD(y, tx, initial w, max_iters, gamma):
  ''' Linear regression using stochastic gradient descent. '''
  return
def least_squares(y, tx):
  ''' Least squares regression using normal equations. '''
  return
def ridge_regression(y, tx, lambda_ ):
  ''' Ridge regression using normal equations. '''
  return
def logistic_regression(y, tx, initial_w, max_iters, gamma):
  ''' Logistic regression using gradient descent or SGD (y in {0,1}). '''
  return
def reg_logistic_regression(y, tx, lambda_ , initial_w, max_iters, gamma):
  ''' Regularized logistic regression using gradient descent or SGD,
      y in {0,1}, with regularization term lambda*||w||^2. '''
  return
