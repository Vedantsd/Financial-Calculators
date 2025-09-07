from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sip-calculator', methods=['GET', 'POST'])
def sip_calc():
    if request.method == 'POST':
        try:
            monthly_investment = float(request.form['monthly_investment'])
            annual_return_rate = float(request.form['annual_return_rate'])
            investment_period_years = int(request.form['investment_period_years'])
            
            monthly_return_rate = annual_return_rate / (12 * 100)  
            total_months = investment_period_years * 12
            
            if monthly_return_rate > 0:
                future_value = monthly_investment * (((1 + monthly_return_rate) ** total_months - 1) / monthly_return_rate) * (1 + monthly_return_rate)
            else:
                future_value = monthly_investment * total_months
            
            total_investment = monthly_investment * total_months
            total_returns = future_value - total_investment
            
            results = {
                'monthly_investment': monthly_investment,
                'annual_return_rate': annual_return_rate,
                'investment_period_years': investment_period_years,
                'future_value': round(future_value, 2),
                'total_investment': round(total_investment, 2),
                'total_returns': round(total_returns, 2)
            }
            
            return render_template('sip-calc.html', results=results)
            
        except (ValueError, KeyError) as e:
            error_message = "Please enter valid numeric values for all fields."
            return render_template('sip-calc.html', error=error_message)
    

    return render_template('sip-calc.html')

@app.route('/stepup-sip-calculator', methods=['GET', 'POST'])
def stepup_sip_calc():
    if request.method == 'POST':
        try:
            initial_investment = float(request.form['initial_investment'])
            annual_step_up = float(request.form['annual_step_up'])
            annual_return_rate = float(request.form['annual_return_rate'])
            investment_period_years = int(request.form['investment_period_years'])
            
            monthly_return_rate = annual_return_rate / (12 * 100)  
            annual_step_up_decimal = annual_step_up / 100  
            total_months = investment_period_years * 12
            
            future_value = 0
            total_investment = 0
            current_monthly_investment = initial_investment
            
            for year in range(investment_period_years):
                for month in range(12):
                    months_remaining = total_months - (year * 12 + month)
                    if monthly_return_rate > 0:
                        month_future_value = current_monthly_investment * ((1 + monthly_return_rate) ** months_remaining)
                    else:
                        month_future_value = current_monthly_investment
                    
                    future_value += month_future_value
                    total_investment += current_monthly_investment
                
                if year < investment_period_years - 1:
                    current_monthly_investment *= (1 + annual_step_up_decimal)
            
            total_returns = future_value - total_investment
            
            avg_monthly_investment = total_investment / total_months
            
            final_monthly_investment = initial_investment
            for year in range(investment_period_years - 1):
                final_monthly_investment *= (1 + annual_step_up_decimal)
            
            results = {
                'initial_investment': initial_investment,
                'annual_step_up': annual_step_up,
                'annual_return_rate': annual_return_rate,
                'investment_period_years': investment_period_years,
                'future_value': round(future_value, 2),
                'total_investment': round(total_investment, 2),
                'total_returns': round(total_returns, 2),
                'avg_monthly_investment': round(avg_monthly_investment, 2),
                'final_monthly_investment': round(final_monthly_investment, 2)
            }
            
            return render_template('stepup-sip-calc.html', results=results)
            
        except (ValueError, KeyError) as e:
            error_message = "Please enter valid numeric values for all fields."
            return render_template('stepup-sip-calc.html', error=error_message)
    
    return render_template('stepup-sip-calc.html')

if __name__ == ("__main__"):
    app.run(debug=True)
