import urllib.request

class IoTController:
    def __init__(self, main_url):
        self.main_url = main_url

    def send_request(self, url):
        urllib.request.urlopen(url)

    def led_on(self, a):
        if a == 4:
            self.send_request(self.main_url + "/turn_on/relay1")
        elif a == 5:
            self.send_request(self.main_url + "/turn_on/relay2")
        elif a == 6:
            self.send_request(self.main_url + "/turn_on/relay3")
        elif a == 7:
            self.send_request(self.main_url + "/turn_on/relay4")

    def led_off(self, a):
        if a == 4:
            self.send_request(self.main_url + "/turn_off/relay1")
        elif a == 5:
            self.send_request(self.main_url + "/turn_off/relay2")
        elif a == 6:
            self.send_request(self.main_url + "/turn_off/relay3")
        elif a == 7:
            self.send_request(self.main_url + "/turn_off/relay4")

    def operate_lights(self, s):
        try:
            if 'turn off' in s:
                if 'music light' in s:
                    self.led_on(4)
                elif 'room light' in s:
                    self.led_on(5)
                elif 'second' in s:
                    self.led_on(6)
                elif 'third' in s:
                    self.led_on(7)
            elif 'turn on' in s:
                if 'room light' in s:
                    self.led_off(5)
                elif 'music light' in s:
                    self.led_off(4)
                elif 'second' in s:
                    self.led_off(6)
                elif 'third' in s:
                    self.led_off(7)
        except:
            pass

if __name__ == "__main__":
    main_url = "http://192.168.43.148"
    iot_controller = IoTController(main_url)

    iot_controller.operate_lights('turn on third')
    # iot_controller.operate_lights('turn off second')
    # iot_controller.operate_lights('turn off music light')
    # iot_controller.operate_lights('turn off room light')
