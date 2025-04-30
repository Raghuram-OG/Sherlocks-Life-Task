from flask import Flask
from flask_cors import CORS
from routes.agents import agents_bp
from routes.onboarding import onboarding_bp
from routes.calls import calls_bp
from routes.key_assignment import key_assignment_bp
from routes.agent_hourly_metrics import agent_hourly_metrics_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(agents_bp, url_prefix="/api")
app.register_blueprint(onboarding_bp, url_prefix="/api")
app.register_blueprint(calls_bp, url_prefix="/api")
app.register_blueprint(key_assignment_bp, url_prefix="/api")
app.register_blueprint(agent_hourly_metrics_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)