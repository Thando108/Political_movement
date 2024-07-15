# Political Movement

## Overview

Political Movement is a Django application designed to manage and track political activities and events. This project aims to provide a platform for organizing political movements, tracking member contributions, and managing events efficiently.

## Prerequisites

- **Python**: 3.11.4
- **Django**: 5.0.3
- **Docker**: 26.1.4

### Dependencies

For a complete list of dependencies, refer to `requirements.txt`. Some of the main packages used include:

- Django 5.0.3
- Sphinx 7.3.7
- numpy 1.26.4
- spacy 3.7.5

## Installation

### Setting up a Virtual Environment

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Thando108/Political_movement.git
   cd Political_movement

   ```

2. **Apply database migrations**:

   ```bash
   python manage.py migrate

   ```

3. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

### Using Docker

1. **Build the Docker image**:

   ```bash
   docker build -t political_movement .

   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 8000:8000 political_movement
   ```

## Usage

The application can be accessed at http://localhost:8000 when running locally.

### Key URLs

- Admin site: http://localhost:8000/admin/
- Main app: [Describe the main app endpoints]
- Accounts: http://localhost:8000/accounts/ (Django authentication)

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

N/A

## Contact

For questions or support, please contact [Thando Mkhize, contact: 0715501305].
