#include <stdlib.h>
#include <stdio.h>
#include <getopt.h>
#include <string.h>

const char *options="hs:t:";
const struct option long_options[]={
	{"help",0,NULL,'h'},
	{"src",1,NULL,'s'},
	{"type",1,NULL,'t'},
	{NULL,0,NULL,0}
};

void help()
{
	printf("author ltw:4/12/2008 d/m/Y\n");
	printf("Usage:\n\tltwbase64 -s string -t e\n\tltwbase64 -s string -t d\n");
	exit(0);
}

static const char Base64[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

void base64_decode(char *src,char *dst)
{
	char *q=malloc(strlen(src)+1);
	char *p=dst;
	char *temp=q;
	char *s=src;
	int len=strlen(src),i;
	memset(q,0,strlen(src)+1);
	while(*s)
	{
		if(*s>='A'&&*s<='Z') *temp=*s-'A';
		else if(*s>='a'&&*s<='z') *temp=*s-'a'+26;
		else if(*s>='0'&&*s<='9') *temp=*s-'0'+52;
		else if(*s=='+') *temp=62;
		else if(*s=='/') *temp=63;
		else if(*s=='=') *temp=-1;
		else
		{
			printf("\n%c:Not a valid base64 string\n",*s);
			exit(0);
		}
		++s;
		++temp;
	}
	for(i=0;i<len-4;i+=4)
	{
		*p++=(*(q+i)<<2)+(*(q+i+1)>>4);
		*p++=(*(q+i+1)<<4)+(*(q+i+2)>>2);
		*p++=(*(q+i+2)<<6)+(*(q+i+3));
	}
	if(*(q+i+3)!=-1)
	{
		*p++=(*(q+i)<<2)+(*(q+i+1)>>4);
		*p++=(*(q+i+1)<<4)+(*(q+i+2)>>2);
		*p++=(*(q+i+2)<<6)+*(q+i+3);
	}
	else if(*(q+i+2)!=-1)
	{
		*p++=(*(q+i)<<2)+(*(q+i+1)>>4);
		*p++=(*(q+i+1)<<4)+(*(q+i+2)>>2);
		*p++=(*(q+i+2)<<6);
	}
	else if(*(q+i+1)!=-1)
	{
		*p++=(*(q+i)<<2)+(*(q+i+1)>>4);
		*p++=(*(q+i+1)<<4);
	}
	else
	{
		printf("Not a valid base64 string\n");
		exit(0);
	}
	*p=0;
	free(q);
}

void base64_encode(const char *src,char *dst)
{
	int i=0;
	char *p=dst;
	int d=strlen(src)-3;
	//for(i=0;i<strlen(src)-3;i+=3) ;if (strlen(src)-3)<0 there is a buf

	for(i=0;i<=d;i+=3)
	{
		*p++=Base64[((*(src+i))>>2)&0x3f];
		*p++=Base64[(((*(src+i))&0x3)<<4)+((*(src+i+1))>>4)];
		*p++=Base64[((*(src+i+1)&0xf)<<2)+((*(src+i+2))>>6)];
		*p++=Base64[(*(src+i+2))&0x3f];
	}
	if((strlen(src)-i)==1)
	{
		*p++=Base64[((*(src+i))>>2)&0x3f];
		*p++=Base64[((*(src+i))&0x3)<<4];
		*p++='=';
		*p++='=';
	}
	if((strlen(src)-i)==2)
	{
		*p++=Base64[((*(src+i))>>2)&0x3f];
		*p++=Base64[(((*(src+i))&0x3)<<4)+((*(src+i+1))>>4)];
		*p++=Base64[((*(src+i+1)&0xf)<<2)];
		*p++='=';
	}
	*p='\0';
}

int main(int argc,char **argv)
{
	opterr=0;
	char option;
	char *src=malloc(100);
	char *dst;
	char type;
	int s=0,t=0;
	while((option=getopt_long(argc,argv,options,long_options,NULL))!=-1)
	{    
		switch(option)
		{
			case 'h':
				help();
				break;
			case 's':
				if(strlen(optarg)>99)
					help();
				strncpy(src,optarg,strlen(optarg));
				*(src+strlen(optarg))='\0';
				s=1;
				break;
			case 't':
				type=optarg[0];
				t=1;
				break;
			case '?':
				break;
			default:
				break;
		}

	}
	dst=malloc(((strlen(src)+2)*4/3)+1);
	if(t&&s&&type=='e')
	{
		base64_encode(src,dst);
		printf("%s\n",dst);
	}
	else if(t&&s&&type=='d')
	{
		base64_decode(src,dst);
		printf("%s\n",dst);
	}
	else
		help();
	free(dst);
}
