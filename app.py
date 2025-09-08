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

@app.route('/swp-calculator', methods=['GET', 'POST'])
def swp_calc():
    if request.method == 'POST':
        try:
            initial_investment = float(request.form['initial_investment'])
            monthly_withdrawal = float(request.form['monthly_withdrawal'])
            annual_return_rate = float(request.form['annual_return_rate'])
            withdrawal_period_years = int(request.form['withdrawal_period_years'])
            
            monthly_return_rate = annual_return_rate / (12 * 100)  
            total_months = withdrawal_period_years * 12
            
            remaining_corpus = initial_investment
            total_withdrawals = 0
            monthly_details = []
            
            for month in range(1, total_months + 1):
                # Calculate interest for the month
                if monthly_return_rate > 0:
                    monthly_interest = remaining_corpus * monthly_return_rate
                    remaining_corpus += monthly_interest
                else:
                    monthly_interest = 0
                
                # Withdraw the monthly amount
                if remaining_corpus >= monthly_withdrawal:
                    remaining_corpus -= monthly_withdrawal
                    total_withdrawals += monthly_withdrawal
                    actual_withdrawal = monthly_withdrawal
                else:
                    # If remaining corpus is less than withdrawal amount
                    actual_withdrawal = remaining_corpus
                    total_withdrawals += actual_withdrawal
                    remaining_corpus = 0
                
                monthly_details.append({
                    'month': month,
                    'opening_balance': remaining_corpus + actual_withdrawal - (monthly_interest if monthly_return_rate > 0 else 0),
                    'interest_earned': monthly_interest if monthly_return_rate > 0 else 0,
                    'withdrawal': actual_withdrawal,
                    'closing_balance': remaining_corpus
                })
                
                # If corpus is exhausted, break
                if remaining_corpus <= 0:
                    break
            
            total_interest_earned = total_withdrawals + remaining_corpus - initial_investment
            
            # Calculate how long the corpus will last
            months_lasted = len(monthly_details)
            years_lasted = months_lasted / 12
            
            results = {
                'initial_investment': initial_investment,
                'monthly_withdrawal': monthly_withdrawal,
                'annual_return_rate': annual_return_rate,
                'withdrawal_period_years': withdrawal_period_years,
                'total_withdrawals': round(total_withdrawals, 2),
                'remaining_corpus': round(remaining_corpus, 2),
                'total_interest_earned': round(total_interest_earned, 2),
                'months_lasted': months_lasted,
                'years_lasted': round(years_lasted, 2),
                'corpus_exhausted': remaining_corpus <= 0,
                'monthly_details': monthly_details[:12]  # Show first 12 months only
            }
            
            return render_template('swp-calc.html', results=results)
            
        except (ValueError, KeyError) as e:
            error_message = "Please enter valid numeric values for all fields."
            return render_template('swp-calc.html', error=error_message)
    
    return render_template('swp-calc.html')

if __name__ == ("__main__"):
    app.run(debug=True)
