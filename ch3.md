Problem Output
Create a function called movie_ticket_sales_tracker that analyzes movie ticket sales data. Given a list of ticket sales, the function should:

1. Calculate total revenue
2. Count total tickets sold
3. Identify the most popular movie type
4. Categorize sales by time of day (morning, afternoon, evening)
5. Determine the peak sales period
6. Calculate average ticket price

Sample Input:
ticket_sales = [
    {'movie_type': 'Action', 'price': 12.50, 'time': '19:30'},
    {'movie_type': 'Comedy', 'price': 10.00, 'time': '14:45'},
    {'movie_type': 'Action', 'price': 12.50, 'time': '20:15'},
    {'movie_type': 'Drama', 'price': 11.00, 'time': '11:30'},
    {'movie_type': 'Comedy', 'price': 10.00, 'time': '16:00'}
]

Expected Output
{
    'total_revenue': 56.00,
    'total_tickets_sold': 5,
    'average_ticket_price': 11.20,
    'movie_type_sales': {'Action': 25.00, 'Comedy': 20.00, 'Drama': 11.00},
    'most_popular_movie_type': 'Action',
    'time_period_sales': {'morning': 11.00, 'afternoon': 20.00, 'evening': 25.00},
    'peak_sales_period': 'evening'
}
