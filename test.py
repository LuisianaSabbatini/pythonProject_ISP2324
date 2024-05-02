import unittest #modulo per unit testing
from OOP import ContoBancario, ContoLibretto #modulo da testare

class TestContoBancario(unittest.TestCase):#dichiarazione della classe dove effettueremo i vari test
    # fino a qua tutto obbligatorio per fare unit testing
    @classmethod
    def setUpClass(cls):
        print('sto eseguendo il setup principale')

    @classmethod                                             
    def tearDownClass(cls):
        print('stiamo eseguendo il teardown principale')

    def setUp(self): #codice che verrà eseguito prima dell'esecuzione di ogni test
        self.conto1 = ContoBancario('Luisiana', 'Sabbatini', 12345, 500)
        print('sto eseguendo il setup')

    def tearDown(self): #codice che verrà eseguito dopo l'esecuzione di ogni test
        print('sto eseguendo il teardown')

    def test_deposito(self): #del tipo "test_nomeFunzione"
        self.conto1.deposito(200)
        self.assertEqual(self.conto1.saldo, 700)
        self.conto1.deposito(100)
        self.assertEqual(self.conto1.saldo, 800)
        print('sto eseguendo il test deposito')
        # self.assertEqual()
        # self.assertGreater()
        # self.assertNotEqual()
        # self.assertIsInstance()

    def test_prelievo(self):
        self.conto1.prelievo(200)
        self.assertEqual(self.conto1.saldo, 300)
        self.conto1.prelievo(100)
        self.assertEqual(self.conto1.saldo, 200)

    def test_email(self):
        self.assertEqual(self.conto1.email, 'luisiana.sabbatini@email.it')
        self.conto1.nomeIntestatario = 'Mario'
        self.assertEqual(self.conto1.email, 'mario.sabbatini@email.it')


        
if __name__ == '__main__': #servono ad eseguire questo codice anche se non c'è espressamente una riga che lo fa eseguire
    unittest.main()
