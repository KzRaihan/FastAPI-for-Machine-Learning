from sklearn.metrics import accuracy_score, classification_report


def evaluation(model, X_test, y_test):
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=0)

    return acc, report

