from website import create_app

app = create_app()

#only if we start this application when this is ran
if __name__ == '__main__':
    #Starts the the application and any change to the application
    #t will rerun the whole application if the debug is set to True turn off when in production
    app.run(debug=True)
    