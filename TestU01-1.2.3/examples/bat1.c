#include "ulcg.h"
#include "unif01.h"
#include "bbattery.h"

int main (void)
{
   unif01_Gen *gen;
   // 2147483647 is 2^31 - 1 
   gen = ulcg_CreateLCG (2147483647, 16807, 0, 1);
   bbattery_SmallCrush (gen);
   ulcg_DeleteGen (gen);
   return 0;
}
