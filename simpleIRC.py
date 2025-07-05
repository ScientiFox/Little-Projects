###
#
# simpleIRC
#  A lightweight and very basic terminal input IRC client,
#  written entirely in python. SUpports basic bots
#
###

#Import for networking
import socket

#Class to hold the connection and data
class IRCClient:

    #Init globals
    socket = None #None made yet
    connected = False #Connection FLag
    nickname = 'RowBot' #Nickname to use online
    channels = ['#foobar', '#barefoot'] #Channels to join

    #Initialization method
    def __init__(self):

        #Start up the socket connecton        
        self.socket = socket.socket()
        self.socket.connect(('irc.rigsofrods.org', 6667)) #IRC to go to
        self.send("NICK %s" % self.nickname) #Send nickname and user setup commands
        self.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s" % {'nick':self.nickname})

        #Loop forever
        while True:
            buf = self.socket.recv(4096) #Get data from stream
            lines = buf.split("\n") #Split the lines
            for data in lines: #for all sent messages in this packet
                data = str(data).strip() #Remove extre whitespace

                if data == '': #Ignore empty lines
                    continue
                print "I<", data #Print message

                # server ping/pong
                if data.find('PING') != -1: #If there's a PING request in there
                    n = data.split(':')[1] #Grab the return string
                    self.send('PONG :' + n) #PONG it back
                    if self.connected == False: #if not connected
                        self.perform() # DO the joins to each channel
                        self.connected = True #set connection flag

                args = data.split(None, 3) #Divide up the message into arguments
                if len(args) != 4: #skip over if not enough data to parse
                    continue
                ctx = {}
                ctx['sender'] = args[0][1:] #Grab sender
                ctx['type']   = args[1] #Grab msg type
                ctx['target'] = args[2] #grab target
                ctx['msg']    = args[3][1:] #Grab message text content

                # Check if targeting user and get sender if so
                target = ctx['target']
                if ctx['target'] == self.nickname:
                    target = ctx['sender'].split("!")[0]

                # A basic command example
                if ctx['msg'] == '!help':
                    self.say('available commands: !help', target)

                # For messages to the bot
                if ctx['type'] == 'PRIVMSG' and (ctx['msg'].lower()[0:len(self.nickname)] == self.nickname.lower() or ctx['target'] == self.nickname):
                    # Something is speaking to the bot
                    query = ctx['msg']
                    if ctx['target'] != self.nickname: #Process a message referring to the user
                        query = query[len(self.nickname):]
                        query = query.lstrip(':,;. ')

                    # Do something here, like query a chatterbot
                    print 'someone spoke to us: ', query #Note query here
                    self.say('alright :|', target) #basic response placeholder

    #Wrapper function to send a message
    def send(self, msg):
        print "I>",msg #Report what you sent
        self.socket.send(msg+"\r\n") #send it

    #Simple response template
    def say(self, msg, to):
        self.send("PRIVMSG %s :%s" % (to, msg))

    def perform(self):
        #self.send("PRIVMSG R : Register <>") #command to register a nick
        self.send("PRIVMSG R : Login <>") #Login
        self.send("MODE %s +x" % self.nickname) #set mode for communication
        for c in self.channels: #Join each channel
            self.send("JOIN %s" % c)
            # say hello to every channel
            self.say('hello world!', c)

#Main function
if __name__ == '__main__':
    IRCClient() #Run the client
