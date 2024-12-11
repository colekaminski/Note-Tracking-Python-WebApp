#Cole Kaminski
#11 December 2024
#Partial Credit to Tech With Tim via YouTube

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#Set debug to false when in production, it is so webpage refershes when code changes