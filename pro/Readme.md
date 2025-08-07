# Django E-commerce Project

A simple e-commerce web application built with Django.  
This project includes user registration, product management, cart, and order processing features.

## Features

- User registration and authentication
- Product categories and images
- Product listing with stock and price
- Shopping cart functionality
- Order placement and payment integration (Razorpay)
- Admin panel for managing products, categories, and orders

## Models

- **Registration**: User details and authentication
- **Category**: Product categories with images and descriptions
- **Product**: Product details, stock, price, and category relation
- **Order**: Order details, user, product, payment info
- **Cart**: User cart and order linkage
- **Img**: Image uploads for testing
- **Student**: Example model for demonstration

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure your database settings in `settings.py`.
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the site at `http://127.0.0.1:8000/`
- Register a new user and start shopping!
- Admin panel available at `/admin`

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For questions or feedback, please contact [your-email@example.com].