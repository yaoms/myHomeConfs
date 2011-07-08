#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/socket.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>

/*
 * 测试 HTTP 协议的简易 Http Server 实现。
 * 只是在标准输出打印出客户端的请求头和响应头。
 * 响应只是一个简单的200信息页面，请求的参数统统被忽略。
 * 单线程运行，同时只能连接一个客户端。
 * 监听本地的8081端口，http://localhost:8081/
 * Yaoms <yms541@gmail.com>
 * 2011年 07月 08日 星期五 10:57:23 CST
 */

unsigned short stop = 0;

void *thread_run(void *arg)
{
    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    int fd;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(8081);
    addr.sin_addr.s_addr = INADDR_ANY;
    if((fd = socket(AF_INET, SOCK_STREAM, 0))==-1)
    {
        fprintf(stderr, "Unable to Open the Socket\n");
        stop = 1;
        return ;
    }
    if (bind(fd, (struct sockaddr*)(&addr), sizeof(addr)) != 0)
    {
        fprintf(stderr, "Unable to bind the Socket\n");
        stop = 1;
        return ;
    }
    if (listen(fd, 50) == -1)
    {
        fprintf(stderr, "Unable to listen the Socket\n");
        stop = 1;
        return ;
    }
    char request[1000];
    while(1){
        struct sockaddr client_addr;
        unsigned int nLength;
        int fdc = accept(fd, &client_addr, &nLength); // block here
        if (fdc == -1){
            fprintf(stderr, "Unable to Connect with the client\n");
            return;
        } else{
            memset(request, 0, 1000);
            read(fdc, request, 1000);
            printf("%s", request);
            char buf[] = "HTTP/1.1 200 OK\r\nServer: HTTP Server BY Yaoms"
                    "\r\nContent-Type: text/html\r\n\r\n"
                    "<h1>This is The Server By Yaoms</h1>\r\n";
            printf("%s", buf);
            printf("-----------\n");
            write(fdc, buf, strlen(buf));
            close(fdc);
        }
    }
}

void child_thread()
{
    pthread_t t;
    pthread_attr_t attr;
    if (pthread_attr_init(&attr) != 0)
        printf("Unable to launch a thread\n");
    if(pthread_create(&t, &attr, thread_run, NULL) != 0)
        printf("Unable to launch a thread\n");
    if(pthread_attr_destroy(&attr) != 0)
        printf("Unable to launch a thread\n");
    if(pthread_detach(t) != 0)
        printf("Unable to launch a thread\n");
}

int main() {
    printf("/*\n * 测试 HTTP 协议的简易 Http Server 实现。\n * 只是在标准输出打印出客户端的请求头和响应头。\n * 响应只是一个简单的200信息页面，请求的参数统统被忽略。\n * 单线程运行，同时只能连接一个客户端。\n * 监听本地的8081端口，http://localhost:8081/\n * Yaoms <yms541@gmail.com>\n * 2011年 07月 08日 星期五 10:57:23 CST\n */\n");
    printf("-----------\n");
    child_thread();
    while(!stop)
    {
        sleep(1);
    }
    return 0;
}
