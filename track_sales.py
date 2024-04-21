import matplotlib.pyplot as plt

class SalesTracker:
    def __init__(self):
        self.sales = {
            'month': {
                'Jan': 0,
                'Feb': 0,
                'Mar': 0,
                'Apr': 0,
                'May': 0,
                'Jun': 0,
                'Jul': 0,
                'Aug': 0,
                'Sep': 0,
                'Oct': 0,
                'Nov': 0,
                'Dec': 0
            },
            'year': {
                2080: 0,
                2081: 0,
                2082: 0
            }
        }

    def add_sale(self, month, year, num_sales):
        self.sales['month'][month] += num_sales
        self.sales['year'][year] += num_sales

    def get_sales(self):
        return self.sales

    def reset_sales(self):
        self.sales = {
            'month': {
                'Jan': 0,
                'Feb': 0,
                'Mar': 0,
                'Apr': 0,
                'May': 0,
                'Jun': 0,
                'Jul': 0,
                'Aug': 0,
                'Sep': 0,
                'Oct': 0,
                'Nov': 0,
                'Dec': 0
            },
            'year': {
                2080: 0,
                2081: 0,
                2082: 0
            }
        }

# Initialize the sales tracker
tracker = SalesTracker()

# Add some sample sales
tracker.add_sale('Jan', 2080, 10)
tracker.add_sale('Feb', 2080, 15)
tracker.add_sale('Mar', 2080, 20)
tracker.add_sale('Jan', 2081, 12)
tracker.add_sale('Feb', 2081, 18)
tracker.add_sale('Mar', 2081, 24)
tracker.add_sale('Jan', 2082, 14)
tracker.add_sale('Feb', 2082, 21)
tracker.add_sale('Mar', 2082, 28)

# Get the total sales for each year
sales_by_year = tracker.get_sales()['year']
sorted_sales_by_year = sorted(sales_by_year.items(), key=lambda x: x[0])

# Plotting the data on a line graph
years = [str(year) for year, _ in sorted_sales_by_year]
sales = [sales for _, sales in sorted_sales_by_year]

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(years, sales, marker='o', color='skyblue')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Growth Over the Years')
plt.grid(True, linestyle='--')

# Adding annotations to the line graph
for i, txt in enumerate(sales):
    plt.annotate(txt, (years[i], sales[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Adding mention of tea sales
plt.text(0.5, 0.5, 'Tea Sales: $30 per serving', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)

# Plotting the data on a pie chart
plt.subplot(1, 2, 2)
sales_by_month = tracker.get_sales()['month']
months = list(sales_by_month.keys())
sales = list(sales_by_month.values())
plt.pie(sales, labels=months, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Sales Distribution by Month')
plt.grid(True, linestyle='--')
plt.show()
