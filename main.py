from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Subscription plans data
plans = [
    {"id": 1, "name": "Starter", "price": 49.0, "features": ["100 orders/month", "2 platforms", "5 creators", "Basic analytics", "Email support"]},
    {"id": 2, "name": "Growth", "price": 99.0, "features": ["500 orders/month", "5 platforms", "10 creators", "Advanced analytics", "Priority support"]},
    {"id": 3, "name": "Pro", "price": 199.0, "features": ["2K orders/month", "8 platforms", "Unlimited creators", "Scan & ship", "Phone support"]},
    {"id": 4, "name": "Enterprise", "price": 399.0, "features": ["Unlimited orders", "8 platforms", "Unlimited creators", "White-label", "Custom integrations"]}
]

platforms = [
    {"name": "TikTok Shop", "status": "active", "orders_synced": 150},
    {"name": "Instagram Shopping", "status": "active", "orders_synced": 89},
    {"name": "Facebook Shop", "status": "active", "orders_synced": 67},
    {"name": "YouTube Shopping", "status": "active", "orders_synced": 34},
    {"name": "Pinterest Shopping", "status": "active", "orders_synced": 23},
    {"name": "Snapchat Commerce", "status": "active", "orders_synced": 12},
    {"name": "Twitter Shopping", "status": "active", "orders_synced": 8},
    {"name": "LinkedIn Shopping", "status": "active", "orders_synced": 5}
]

@app.route('/')
def home():
    return jsonify({"message": "SyncMaster Suite API", "status": "operational", "version": "1.0.0"})

@app.route('/api/billing/plans')
def get_plans():
    return jsonify({"success": True, "plans": plans})

@app.route('/api/platforms/available')
def get_platforms():
    return jsonify({"success": True, "platforms": platforms})

@app.route('/api/admin/dashboard')
def admin_dashboard():
    return jsonify({
        "success": True,
        "system_health": {"api_status": "operational", "database": "healthy", "integrations": "active"},
        "metrics": {"total_users": 1247, "active_subscriptions": 892, "monthly_revenue": 89650.0}
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
