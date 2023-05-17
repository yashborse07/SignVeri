    print('Genuine Image')
                    return True
                else:
                    print('Forged Image')
                    return False

    def trainAndTest(rate=0.001, epochs=1700, neur