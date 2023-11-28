import telegram.ext 
Token = "6832089895:AAHrP6hlmqrk6IcSE3umD62f9k0rD7G1kuY"

updater = telegram.ext.Updater("P6832089895:AAHrP6hlmqrk6IcSE3umD62f9k0rD7G1kuY", use_context=True)
disp = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to Howw toooooo !!")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /content -> How to provides videos about How tos
    /sing  -> Video link to a how to sing video on youtube
    /rap -> Video link to a how to rap video on youtube
    /dance -> Video link to a how to dance video on youtube
    /draw -> Video link to a how to draw video on youtube
    /contact -> contact information 
     """)
    
def content(update, context):
    update.message.reply_text("We have various videos available!")

def sing(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/jog-nfLldRI?si=CFWca7R1u0VOhE7G")

def rap(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/c6-hr6TaIUM?si=ee2_ntk2VULHi3bV ")
    
def dance(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/C62596gVnT8?si=1bB8QVFkcF-5o5xc")
    
def draw(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/1jjmOF1hQqI?si=3mYAncuTXN7U2_j8")

def contact(update, context):
    update.message.reply_text("You can contact on email : kellylouis****** ")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('content',content))
disp.add_handler(telegram.ext.CommandHandler('sing',sing))
disp.add_handler(telegram.ext.CommandHandler('rap',rap))
disp.add_handler(telegram.ext.CommandHandler('dance',dance))
disp.add_handler(telegram.ext.CommandHandler('draw',draw))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle() 