from flask import Flask, request, jsonify
from flask_cors import CORS
from agents import financial_analyst, market_research_analyst, reporting_analyst

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route("/generate", methods=["POST"])
def generate_report():
    try:
        data = request.json
        company = data.get("company", "").strip()

        if not company:
            return jsonify({"error": "No company provided"}), 400

        # Run agents sequentially
        financial = financial_analyst(company)
        market = market_research_analyst(company)

        # Reporting analyst can take into account previous outputs
        summary_input = f"""
        Financial Analysis:
        {financial}

        Market Analysis:
        {market}
        """
        summary = reporting_analyst(summary_input)

        return jsonify({
            "company": company,
            "financial_analysis": financial,
            "market_analysis": market,
            "summary_report": summary
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
