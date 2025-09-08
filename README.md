# Financial Calculators

A comprehensive web application built with Flask for various financial calculations. Features SIP (Systematic Investment Plan) and SWP (Systematic Withdrawal Plan) calculators with responsive design optimized for all devices.

## 🚀 Features

### 1. **SIP Calculator**
- Calculate returns for regular monthly investments
- Compound interest calculations
- Detailed breakdown of investment vs. returns

### 2. **Step-up SIP Calculator**
- Progressive SIP with annual increment feature
- Year-by-year calculation with step-up growth
- Advanced analytics including average monthly investment

### 3. **SWP Calculator**
- Systematic Withdrawal Plan for retirement planning
- Calculate sustainable withdrawal amounts from investments
- Month-by-month breakdown with interest calculations
- Corpus exhaustion warnings and timeline predictions

## 💻 Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Responsive Design
- **Styling**: Custom CSS with mobile-first approach
- **Architecture**: MVC pattern with template inheritance

## 📱 Responsive Design

- **Mobile-First**: Optimized for phone screens
- **Breakpoints**: 768px (tablets) and 480px (mobile)
- **Grid Layout**: Adaptive 2-column to 1-column layout
- **Touch-Friendly**: Large buttons and input fields

## 🏗️ Project Structure

```
Financial Calculators/
├── app.py                          # Flask application with routes
├── static/
│   └── styles.css                  # Reusable responsive CSS
├── templates/
│   ├── index.html                  # Home page with calculator tiles
│   ├── sip-calc.html              # Regular SIP calculator
│   ├── stepup-sip-calc.html       # Step-up SIP calculator
│   └── swp-calc.html              # SWP calculator
├── .gitignore                      # Git ignore file
├── LICENSE                         # MIT License file
└── README.md                       # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vedantsd/Financial-Calculators.git
   cd Financial-Calculators
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:5000`

## 📊 Calculator Features

### SIP Calculator
- **Monthly Investment**: ₹100 - unlimited
- **Annual Return**: 1% - 30%
- **Investment Period**: 1 - 50 years
- **Results**: Maturity amount, total investment, total returns

### Step-up SIP Calculator
- **Initial Investment**: Starting monthly amount
- **Annual Step-up**: 1% - 50% yearly increase
- **Advanced Metrics**: Average monthly SIP, final monthly amount
- **Detailed Analysis**: Year-by-year growth calculation

### SWP Calculator
- **Initial Investment**: ₹10,000 - unlimited
- **Monthly Withdrawal**: ₹1,000 - unlimited
- **Annual Return**: 1% - 30%
- **Withdrawal Period**: 1 - 50 years
- **Results**: Total withdrawals, remaining corpus, interest earned
- **Smart Features**: Corpus exhaustion alerts, monthly breakdown table

## 🎨 Design Features

- **Modern UI**: Gradient backgrounds and smooth animations
- **User Experience**: Form validation, error handling, value persistence
- **Professional Layout**: Card-based design with clear visual hierarchy
- **Accessibility**: Proper labels, semantic HTML, keyboard navigation

## 📈 Sample Calculations

### Regular SIP Example:
- Monthly Investment: ₹5,000
- Annual Return: 12%
- Period: 10 years
- **Result**: ₹11,61,695 (Total Returns: ₹5,61,695)

### Step-up SIP Example:
- Initial Investment: ₹5,000
- Step-up: 10% annually
- Annual Return: 12%
- Period: 10 years
- **Result**: ₹16,87,163 (Total Returns: ₹7,30,918)

### SWP Example:
- Initial Investment: ₹10,00,000
- Monthly Withdrawal: ₹15,000
- Annual Return: 8%
- Period: 10 years
- **Result**: Total Withdrawals: ₹18,00,000, Remaining Corpus: ₹4,39,117

## 🔮 Future Enhancements

- [ ] EMI Calculator
- [ ] PPF Calculator
- [ ] Tax Calculator
- [ ] Investment Comparison Tool
- [ ] Data Visualization Charts
- [ ] Export Results to PDF
- [ ] SWP with Variable Withdrawal Amounts
- [ ] Inflation-Adjusted Calculations

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Vedant Desai**
- GitHub: [@Vedantsd](https://github.com/Vedantsd)

## 🙏 Acknowledgments

- Thanks to the Flask community for the excellent documentation
- Inspired by various financial planning tools

---

⭐ **Star this repo if you found it helpful!**
