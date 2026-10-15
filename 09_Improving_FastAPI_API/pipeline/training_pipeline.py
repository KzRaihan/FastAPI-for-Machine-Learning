from src.components.model_trainer import train_model
from src.components.model_evaluation import evaluation
from src.components.model_pusher import save_model


def run_training_pipeline():
    model, X_test, y_test = train_model()          
    acc, report = evaluation(model, X_test, y_test)
    print(f"Test accuracy: {acc:.2f}")
    print(report)
    
    path = save_model(model)                        
    print(f"Model saved to: {path}")

