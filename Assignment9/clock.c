//Clock using threads

#include<stdlib.h>
#include<stdio.h>
#include<pthread.h> // for using pthread_mutex
#include<unistd.h>
#include<time.h> // to use localtime() to get current time 



pthread_mutex_t lock;
int seconds, minutes, hours;

void* increment_hr(void* pString) {
    pthread_mutex_lock(&lock);
    if(minutes > 59){
        hours++;
        minutes = 0;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

void* increment_min(void* pString) {
    pthread_mutex_lock(&lock);
    if(seconds > 59) {
        minutes++;
        seconds = 0;
    }
    pthread_mutex_unlock(&lock);
    return 0;
}

void* increment_sec(void* pString) {
    pthread_mutex_lock(&lock);
    //to reset the clock after 23:59:59
    if(seconds == 59 && minutes == 59 && hours == 23){
        hours = 0;
        minutes = 0;
        seconds = -1; // so that it starts on 0 after increment
    }
    seconds++;
    pthread_mutex_unlock(&lock);
    return 0;
}


int main() {
	
	time_t rawtime;
    struct tm * curr_timeinfo;

    time (&rawtime);
    curr_timeinfo = localtime (&rawtime);
    // to get the current time in our variables hours, minutes and seconds
    hours = curr_timeinfo->tm_hour;
    minutes = curr_timeinfo->tm_min;
	seconds = curr_timeinfo->tm_sec;

    pthread_t second_thread, minute_thread, hour_thread; // identify the threads
    printf("--Clock--\n");
	printf("HH:MM:SS\n");
    while(1) {
        sleep(1);
        pthread_create(&second_thread, NULL, increment_sec, NULL);
        pthread_join(second_thread, NULL);
        pthread_create(&minute_thread, NULL, increment_min, NULL);
        pthread_join(minute_thread, NULL);
        pthread_create(&hour_thread, NULL, increment_hr, NULL);
        pthread_join(hour_thread, NULL);
        
        
        printf("%2d:%2d:%2d\n", hours, minutes, seconds);
    }
    pthread_mutex_destroy(&lock);
    return 0;
}
