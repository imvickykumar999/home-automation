
# pip install imvickykumar999
# C:\Users\Vicky\anaconda3\Lib\site-packages\vicksbase

class HomeAutomation:
    def __init__(self, link):

        try:
            from vicksbase import firebase as f
            self.link = link
            self.firebase_obj = f.FirebaseApplication(self.link, None)
            print(self.pull(child = '/'))

        except Exception as e:
            print(e)
            print('try: pip install imvickykumar999')

    def show(self):
        return "Hello, link is... " + self.link

    def pull(self, child = 'A/B/C/Switch'):
        result = self.firebase_obj.get(f'{child}', None)
        return result

    def push(self, data = 1, child = 'A/B/C/Switch'):
        self.firebase_obj.put('/', child, data)
        return f"{self.pull(child = '/')}, ...is present"

    def remove(self, child = 'A/B/C/led2'):
        data = self.firebase_obj.delete('/', child)
        return f"{self.pull(child = '/')}, ...is present"


# link = 'https://led-blink-wifi-default-rtdb.firebaseio.com/'
# obj = HomeAutomation(link)

# f = obj.show()
# f = obj.pull()
# f = obj.push(1)
# f = obj.remove()

# print(f)
# input('Press Enter to Exit...')
