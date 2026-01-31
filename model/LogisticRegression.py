"""
Logistic Regression Model - Trained on UCI Bank Marketing Dataset
Features: 20
Classes: 0 (No Subscription), 1 (Subscription)
"""
import numpy as np
import pickle
import base64

# Model weights and parameters saved as base64-encoded pickle
MODEL_PICKLE_B64 = "gAWVBwMAAAAAAACMHnNrbGVhcm4ubGluZWFyX21vZGVsLl9sb2dpc3RpY5SMEkxvZ2lzdGljUmVncmVzc2lvbpSTlCmBlH2UKIwHcGVuYWx0eZSMCmRlcHJlY2F0ZWSUjAFDlEc/8AAAAAAAAIwIbDFfcmF0aW+URwAAAAAAAAAAjARkdWFslImMA3RvbJRHPxo24uscQy2MDWZpdF9pbnRlcmNlcHSUiIwRaW50ZXJjZXB0X3NjYWxpbmeUSwGMDGNsYXNzX3dlaWdodJROjAxyYW5kb21fc3RhdGWUSyqMBnNvbHZlcpSMBWxiZmdzlIwIbWF4X2l0ZXKUTegDjAd2ZXJib3NllEsAjAp3YXJtX3N0YXJ0lImMBm5fam9ic5ROjA5uX2ZlYXR1cmVzX2luX5RLFIwIY2xhc3Nlc1+UjBNudW1weS5fY29yZS5udW1lcmljlIwLX2Zyb21idWZmZXKUk5QolggAAAAAAAAAAAAAAAEAAACUjAVudW1weZSMBWR0eXBllJOUjAJpNJSJiIeUUpQoSwOMATyUTk5OSv////9K/////0sAdJRiSwKFlGgHdJRSlIwHbl9pdGVyX5RoGSiWBAAAAAAAAAAJAAAAlGggSwGFlGgHdJRSlIwFY29lZl+UaBkolqAAAAAAAAAACITJPYVNub/Rx1rqpSDlv9oMicT2dda/L6L94SfYtj9oCvl0m2HXvyO/VXjoVaO/s1J2JkFh3798LKrM9Hihv1kjkdjSsKK/m+sW7e5exb85CVdQJbK3P3H3Yv4d2dA/crgo2bO73T+4aRqYIqzQP4M4480JmcG/OhAHQ9+Tzb/u1RSeYvvRv7hJovEqqOY/R3qwbNCg4D/APsa+awfnP5RoHYwCZjiUiYiHlFKUKEsDaCFOTk5K/////0r/////SwB0lGJLAUsUhpRoB3SUUpSMCmludGVyY2VwdF+UaBkolggAAAAAAAAAbDqTwaGFsb+UaC9LAYWUaAd0lFKUjBBfc2tsZWFybl92ZXJzaW9ulIwFMS44LjCUdWIu"

class LogisticRegression:
    """Trained Logistic Regression model"""
    
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
model = LogisticRegression()
