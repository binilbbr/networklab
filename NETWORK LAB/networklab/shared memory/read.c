
#include <stdio.h>
#include <sys/shm.h>
#include <sys/stat.h>

int main ()
{
  key_t shm_key = 6166529;
  const int shm_size = 1024;

  int shm_id;
  char* shmaddr, *ptr;
  char* shared_memory[3];
  int *p;

  
  shm_id = shmget (shm_key, shm_size, IPC_CREAT | S_IRUSR | S_IWUSR);

  
  shmaddr = (char*) shmat (shm_id, 0, 0);

  printf ("shared memory attached at address %p\n", shmaddr);

  
  p = (int *)shmaddr;
  ptr = shmaddr + sizeof (int) * 2;
  shared_memory[0] = ptr;
  ptr += *p++;
  shared_memory[1] = ptr;
  ptr += *p;
  shared_memory[2] = ptr;
  printf ("0=%s\n", shared_memory[0]);
  printf ("1=%s\n", shared_memory[1]);
  printf ("2=%s\n", shared_memory[2]);

 
  shmdt (shmaddr);
   shmctl (shm_id, IPC_RMID, 0);
  return 0;
}


