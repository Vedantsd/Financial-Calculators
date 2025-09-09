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
            yearly_details = []
            
            for year in range(1, withdrawal_period_years + 1):
                year_opening_balance = remaining_corpus
                year_total_withdrawals = 0
                year_total_interest = 0
                
                for month in range(12):
                    if remaining_corpus <= 0:
                        break
                        
                    if monthly_return_rate > 0:
                        monthly_interest = remaining_corpus * monthly_return_rate
                        remaining_corpus += monthly_interest
                        year_total_interest += monthly_interest
                    else:
                        monthly_interest = 0
                    
                    if remaining_corpus >= monthly_withdrawal:
                        remaining_corpus -= monthly_withdrawal
                        total_withdrawals += monthly_withdrawal
                        year_total_withdrawals += monthly_withdrawal
                        actual_withdrawal = monthly_withdrawal
                    else:
                        actual_withdrawal = remaining_corpus
                        total_withdrawals += actual_withdrawal
                        year_total_withdrawals += actual_withdrawal
                        remaining_corpus = 0
                
                yearly_details.append({
                    'year': year,
                    'opening_balance': year_opening_balance,
                    'total_withdrawals': year_total_withdrawals,
                    'total_interest': year_total_interest,
                    'closing_balance': remaining_corpus
                })
                
                if remaining_corpus <= 0:
                    break
            
            total_interest_earned = total_withdrawals + remaining_corpus - initial_investment
            
            months_lasted = sum(1 for year_data in yearly_details for _ in range(12) if year_data['closing_balance'] > 0 or year_data['year'] == yearly_details[0]['year'])
            years_lasted = len(yearly_details)
            
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
                'yearly_details': yearly_details
            }
            
            return render_template('swp-calc.html', results=results)
            
        except (ValueError, KeyError) as e:
            error_message = "Please enter valid numeric values for all fields."
            return render_template('swp-calc.html', error=error_message)
    
    return render_template('swp-calc.html')

@app.route('/emi-calculator', methods=['GET', 'POST'])
def emi_calc():
    if request.method == 'POST':
        try:
            loan_amount = float(request.form['loan_amount'])
            annual_interest_rate = float(request.form['annual_interest_rate'])
            loan_tenure_years = int(request.form['loan_tenure_years'])
            
            monthly_interest_rate = annual_interest_rate / (12 * 100)
            total_months = loan_tenure_years * 12
            
            if monthly_interest_rate > 0:
                emi = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** total_months)) / (((1 + monthly_interest_rate) ** total_months) - 1)
            else:
                emi = loan_amount / total_months
            
            total_payment = emi * total_months
            total_interest = total_payment - loan_amount
            
            yearly_schedule = []
            remaining_principal = loan_amount
            
            for year in range(1, loan_tenure_years + 1):
                year_opening_balance = remaining_principal
                year_total_emi = 0
                year_total_principal = 0
                year_total_interest = 0
                
                for month in range(12):
                    if remaining_principal <= 0:
                        break
                        
                    if monthly_interest_rate > 0:
                        interest_component = remaining_principal * monthly_interest_rate
                        principal_component = emi - interest_component
                    else:
                        interest_component = 0
                        principal_component = emi
                    
                    remaining_principal -= principal_component
                    year_total_emi += emi
                    year_total_principal += principal_component
                    year_total_interest += interest_component
                
                yearly_schedule.append({
                    'year': year,
                    'opening_balance': year_opening_balance,
                    'total_emi': year_total_emi,
                    'total_principal': year_total_principal,
                    'total_interest': year_total_interest,
                    'closing_balance': max(0, remaining_principal)
                })
            
            results = {
                'loan_amount': loan_amount,
                'annual_interest_rate': annual_interest_rate,
                'loan_tenure_years': loan_tenure_years,
                'emi': round(emi, 2),
                'total_payment': round(total_payment, 2),
                'total_interest': round(total_interest, 2),
                'yearly_schedule': yearly_schedule
            }
            
            return render_template('emi-calc.html', results=results)
            
        except (ValueError, KeyError) as e:
            error_message = "Please enter valid numeric values for all fields."
            return render_template('emi-calc.html', error=error_message)
    
    return render_template('emi-calc.html')

if __name__ == ("__main__"):
    app.run(debug=True)
