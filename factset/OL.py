## script to read my email

 

def getOrder():

    import win32com.client

    from win32com.client import Dispatch

    from datetime import date

 

    today = date.today()

    outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")

    root_folder = outlook.Folders.Item(1)

    #print (root_folder.Name)

 

    inbox = root_folder.Folders['Inbox']

    non_support = inbox.Folders['Non-Support']

    grub = non_support.Folders['GrubHub/FactSet auto emails']

    #print(grub)

    resturant=''

   

    for message in grub.Items:

        if (str(message.ReceivedTime).split(' ')[0] == str(today)): ## need to switch hardcoded date to today

            if 'Your order' in message.subject:

                step1=message.subject.split('from ')

                step2 = step1[1].split(' has')

                resturant = step2[0]

    return(resturant)

 

def getFriendOrder():

    import win32com.client

    from win32com.client import Dispatch

    from datetime import date

 

    today = date.today()

    outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")

    root_folder = outlook.Folders.Item(1)

 

    inbox = root_folder.Folders['Inbox']

    non_support = inbox.Folders['Non-Support']

    grub = non_support.Folders['GrubHub/FactSet auto emails']

    person = ''

    for message in grub.Items:

        if (str(message.ReceivedTime).split(' ')[0] == str(today)): ## need to switch hardcoded date to today

            if 'Your line of credit' in message.subject:

                text = message.body.split(' ')

                person = (" And I shared "+ str(text[11])+' with '+str(text[8]))

    return(person)                

               

       

 

#getOrder()

#getFriendOrder()