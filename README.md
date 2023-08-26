# U2 (Underground)

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)

## Requirements

1. Python 3.7.0
2. Flask 2.2.5
3. SQLAlchemy 2.0.19
4. Install requirements from : pip install -r requirements.txt`
   
## Installation

1. Clone the repository: `git clone https://github.com/dessufalte/unandeground.git`
2. Navigate to the project directory: `cd unandeground`
3. Run the project from `run.py`

## Features

- **Create Account**: Users can create a new account with a username and password.
- **Edit Account**: Users can edit their account information, including username and password.
- **Create Thread**: Users can create a new thread with a title and content.
- **Comment Thread**: Users can comment on existing threads.
- **Reply to Comment**: Users can reply to existing comments.
- **Vote Statistics**: Users can view vote statistics (upvotes and downvotes) for a specific thread.
- **Tags**: Threads can be tagged for specific categories or topics.

## Contributing

1. Implement your changes. You can find the HTML templates in the templates folder. To add new features, create a new Python file in the format feature_{feature_name}.py. For styling, you can place your CSS files in the static folder.
2. Test your changes locally to ensure they work as expected.
3. Commit your changes with clear commit messages: `git commit -m "Add feature: Your feature description"`
4. Push your changes to your forked repository: `git push origin feature/your-feature-name`
5. Create a Pull Request (PR) to the main branch of the original repository.
6. Once your PR is approved, it will be merged into the main repository.
7. To reset the database, you can run the `reset.py` script in the database management. 

