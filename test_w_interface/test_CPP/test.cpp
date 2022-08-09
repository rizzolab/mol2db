#include <iostream>
#include <pqxx/pqxx> 

using namespace std;
using namespace pqxx;

int main(int argc, char* argv[]) {
    char * sql;
   try {
      connection C("dbname = spak user = spak password = KapSat2400180000\
      hostaddr = 127.0.0.1 port = 5432");
      if (C.is_open()) {
         cout << "Opened database successfully: " << C.dbname() << endl;
      } else {
         cout << "Can't open database" << endl;
         return 1;
      }
      /* Create SQL statement */
      sql = "SELECT * from example";
      
      /* Create a non-transactional object. */
      nontransaction N(C);
       
      /* Execute SQL query */
      result R( N.exec( sql ));

      for (result::const_iterator c = R.begin(); c != R.end(); ++c) {
          std::cout << "ID = " << c[0].as<int>() << endl;
      }
      std::cout << "Operation done successfully" << endl;
      C.disconnect ();
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }
}
