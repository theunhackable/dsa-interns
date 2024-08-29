#include <stdio.h>

int heap[100];
int size = 0;

void swap(int *a, int *b)
{
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}

void insert(int value)
{
  int index; // acts as a pointer for going to the parent node of a particular child node
  heap[size] = value;
  index = size;
  size = size + 1;
  while (index >= 1)
  {
    int parent = (index - 1) / 2;
    if (heap[parent] < heap[index])
    {
      swap(&heap[parent], &heap[index]);
      index = parent;
    }
    else
    {
      return;
    }
  }
}

void delete()
{
  // step1: take the last element and place it as the first element
  heap[0] = heap[size - 1];
  heap[size - 1] = 0;
  --size;
  int ind = 0;
  //  heapify down
  // children of current ind, replace the current val with the max child
  while (ind < size - 1)
  {

    int left_child_ind = 2 * ind + 1;
    int right_child_ind = 2 * ind + 2;

    int current_val = heap[ind];
    int left_child_val = heap[left_child_ind];
    int right_child_val = heap[right_child_ind];

    if (left_child_val > right_child_val && current_val < left_child_val)
    {
      swap(&heap[ind], &heap[left_child_ind]);
      ind = left_child_ind;
    }
    else if (right_child_ind < size && right_child_val > left_child_val && current_val < right_child_val)
    {
      swap(&heap[ind], &heap[right_child_ind]);
      ind = right_child_ind;
    } else {
      break;
    }
  }
}
void print()
{
  for (int i = 0; i < size; i++)
  {
    printf("%d ", heap[i]);
  }
}

int main()
{

  printf("\n");
  insert(50);
  insert(55);
  insert(53);
  insert(52);
  insert(54);
  print();
  delete();
  printf("\n");
  print();
  return 0;
}