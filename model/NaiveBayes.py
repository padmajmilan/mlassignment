"""
Naive Bayes Model - Trained on UCI Bank Marketing Dataset
Features: 20
Classes: 0 (No Subscription), 1 (Subscription)
"""
import numpy as np
import pickle
import base64

# Model weights and parameters saved as base64-encoded pickle
MODEL_PICKLE_B64 = "gAWVnQQAAAAAAACME3NrbGVhcm4ubmFpdmVfYmF5ZXOUjApHYXVzc2lhbk5ClJOUKYGUfZQojAZwcmlvcnOUTowNdmFyX3Ntb290aGluZ5RHPhEuC+gm1pWMCGNsYXNzZXNflIwTbnVtcHkuX2NvcmUubnVtZXJpY5SMC19mcm9tYnVmZmVylJOUKJYIAAAAAAAAAAAAAAABAAAAlIwFbnVtcHmUjAVkdHlwZZSTlIwCaTSUiYiHlFKUKEsDjAE8lE5OTkr/////Sv////9LAHSUYksChZSMAUOUdJRSlIwObl9mZWF0dXJlc19pbl+USxSMCGVwc2lsb25flIwWbnVtcHkuX2NvcmUubXVsdGlhcnJheZSMBnNjYWxhcpSTlGgOjAJmOJSJiIeUUpQoSwNoEk5OTkr/////Sv////9LAHSUYkMIl9Ym6AsuET6UhpRSlIwGdGhldGFflGgKKJZAAQAAAAAAAM2OPW9LAJA/3b+ifv/sxz8Y7J8joYquP2DYv5E9FbW/cseYrUPBwz+mfPeKhx2rPzI/g1znLL0/Mfk/D4rHpz/mnQx1uMCKP+DfHwHGqo6/praabF1gpj9lg+RLo7envwYVYdIVwaS/C+olTog7pr9jVWVQb5+hv51NbxewZps/6lwWjLJ0uz9KxVbZGf7Lv+vZ1X+CWMe/UAkD8F83yL/qjj1vSwCQv92/on7/7Me/E+yfI6GKrr9i2L+RPRW1P3LHmK1DwcO/w3z3iocdq786P4Nc5yy9vzr5Pw+Kx6e/9p0MdbjAir/A3x8BxqqOP6W2mmxdYKa/YIPkS6O3pz8WFWHSFcGkP/3pJU6IO6Y/blVlUG+foT+GTW8XsGabv+NcFoyydLu/SsVW2Rn+yz/q2dV/gljHP08JA/BfN8g/lGgfSwJLFIaUaBV0lFKUjAR2YXJflGgKKJZAAQAAAAAAAFINlsmXMes/TU4g6LyF6z8RK4JyxSbtP6SgQw5VZ/Q/l0TLEQjr6z9wv1GdyXH0P0UeU0NIde4/KrDG9/Re6z+BiF5QNITwP0lmemByOe0/CPsktH3T8j/WPiVAoyTwP8GpkYCoG/I/efDP7wSE7j8KjcdvyJLwP/TtahhF4uw/aY0Q4ANm7D9VlfU1ff3vP5ps7NEZM+o/TGcESOxC7j/hbeIINGXyPy5tEOToHvE/RpCUAHdP8T8JE0dtNsLmP/KkMv5aR/E/nIp65nju5j8MDXZV9VrwPwm78NHZPvI/utTIqcv07j8uUiKUcGHxP3QIe1O5Oeo/fEegT5GT7z9ZCUMvw63rPz4fdT6LrvA/CotBIAbH7j/ZfqjP/4jxP04jBrXDbvE/chn3H+3y7D/uzhkR8NXxP2LSsMGlcu8/lGgfSwJLFIaUaBV0lFKUjAxjbGFzc19jb3VudF+UaAoolhAAAAAAAAAAAAAAAAAAREAAAAAAAABEQJRoH0sChZRoFXSUUpSMDGNsYXNzX3ByaW9yX5RoCiiWEAAAAAAAAAAAAAAAAADgPwAAAAAAAOA/lGgfSwKFlGgVdJRSlIwQX3NrbGVhcm5fdmVyc2lvbpSMBTEuOC4wlHViLg=="

class NaiveBayes:
    """Trained Naive Bayes model"""
    
    def __init__(self):
        """Initialize model from saved weights"""
        import pickle
        import base64
        model_data = base64.b64decode(MODEL_PICKLE_B64)
        self.model = pickle.loads(model_data)
    
    def predict(self, X):
        """Make predictions on input data (X should be scaled)"""
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """Get prediction probabilities"""
        return self.model.predict_proba(X)

# Initialize model instance
model = NaiveBayes()
