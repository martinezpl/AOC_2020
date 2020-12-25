#include <iostream>
#define PK_CARD 10943862
#define PK_DOOR 12721030
#define BORDER 20201227
using namespace std;

int main() {
  unsigned long public_key[2] = { 1, 1 };
  unsigned long encryption_key[2] = { 1, 1 };
  int idx = 0;
  while(1) {
    public_key[0] = (public_key[0] * 7) % BORDER;
    public_key[1] = (public_key[1] * 7) % BORDER;
    encryption_key[0] = ( encryption_key[0] * PK_DOOR ) % BORDER;
    encryption_key[1] = ( encryption_key[1] * PK_CARD ) % BORDER;
    if ( public_key[0] == PK_CARD ) { break; }
    if ( public_key[1] == PK_DOOR ) { idx = 1; break; }
  }
  cout << "encryption key: " <<  encryption_key[idx] << endl;
}
