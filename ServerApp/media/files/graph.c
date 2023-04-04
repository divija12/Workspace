#include <stdio.h>
#include <stdlib.h>

struct node
{
    int vertex;
    struct node* next;
};
struct Graph
{
    struct node** adjLst;
    int *visited;
    int numVertices;
};
struct node* createNode(int num)
{
    struct node* newNode = malloc(sizeof(struct node));
    newNode->next = NULL;
    newNode->vertex = num;
    return newNode;
}
struct Graph* createGraph(int n)
{
    struct Graph* graph = malloc(sizeof(struct Graph));
    graph->numVertices = n;
    graph->adjLst = malloc(n * sizeof(struct node));
    graph->visited = malloc(n * sizeof(int));
    int i;
    for(i=0;i<n;i++)
    {
        graph->visited[i] = 0;
        graph->adjLst[i] = NULL;
    }
    return graph;
}
void addEdge(struct Graph* graph, int src, int dest)
{
    //src to dest add edge
    struct node* newNode = createNode(dest);
    newNode->next = graph->adjLst[src];
    graph->adjLst[src] = newNode;

/*
    //dest to src add edge
    newNode = createNode(src);
    newNode->next = graph->adjLst[dest];
    graph->adjLst[dest] = newNode;
*/
}
struct Queue
{
    int items[20];
    int front, rear;
};
struct Queue* createQueue()
{
    struct Queue* q = malloc(sizeof(struct Queue));
    q->front = -1;
    q->rear = -1;
    return q;
}
int isEmpty(struct Queue* q)
{
    if(q->front == -1)
        return 1;
    return 0;
}
void enqueue(struct Queue* q, int n)
{
    if(q->front == -1)
        q->front += 1;
    q->rear++;
    q->items[q->rear] = n;
}
int dequeue(struct Queue* q)
{
    int temp = q->items[q->front];
    q->front += 1;
    if (q->front > q->rear)
        q->front = q->rear = -1;
    return temp;
}
int out_degree(struct Graph* graph, int vertex)
{
    struct node* temp = graph->adjLst[vertex];
    int count = 0;
    while(temp)
    {
        count++;
        temp = temp->next;
    }
    return count;
}
int in_degree(struct Graph* graph, int v)
{
    int count = 0;
    for(int i = 0; i<graph->numVertices; i++)
    {
        if(v != i)
        {
            struct node* temp = graph->adjLst[i];
            while(temp)
            {
                if(temp->vertex == v)
                    count++;
                temp = temp->next;
            }
        }
    }
    return count;
}
void printQueue(struct Queue* q)
{
    printf("\nQueue: ");
    int i;
    for(i = q->front; i <= q->rear; i++)
        printf("%d  ", q->items[i]);
}
void bfs(struct Graph* graph, int startvertex)
{
    struct Queue* queue = createQueue();

    graph->visited[startvertex] = 1;
    enqueue(queue, startvertex);
    while(isEmpty(queue) == 0)
    {
        //printQueue(queue);
        int currentVertex = dequeue(queue);
        printf("\nVisited: %d", currentVertex);

        struct node* temp = graph->adjLst[currentVertex];

        while(temp!=NULL)
        {
            int adjVertex = temp->vertex;
            if(graph->visited[adjVertex] == 0)
            {
                graph->visited[adjVertex] = 1;
                enqueue(queue, adjVertex);
            }
            temp = temp->next;
        }
    }
}
int main() {
  struct Graph* graph = createGraph(6);
  addEdge(graph, 0, 1);
  addEdge(graph, 0, 2);
  addEdge(graph, 1, 2);
  addEdge(graph, 1, 4);
  addEdge(graph, 1, 3);
  addEdge(graph, 2, 4);
  addEdge(graph, 3, 4);

  bfs(graph, 1);
  printf("\nout-degree of 0: %d", out_degree(graph,0));
  printf("\nout-degree of 1: %d", out_degree(graph,1));
  printf("\nout-degree of 2: %d", out_degree(graph,2));
  printf("\nout-degree of 3: %d", out_degree(graph,3));
  printf("\nout-degree of 4: %d", out_degree(graph,4));

  return 0;
}