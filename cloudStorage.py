import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Aluyt7KJZ0ZYxUg2n1Wb48siEGHIz21qvgAYGSAzU5cRa56Cxc3duI1tF7XImrkGlUqQHtR_noOeJlekgGZNkf0hfxEmfmRIEf2YWwfqdltAka6UtdioGzHy4S6Qas5ovDGlXNo'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : ")
    file_to = input("Enter the full path to upload to Dropbox : ")

    transferData.upload_file(file_from,file_to)
    print("File has been moved!")

main()