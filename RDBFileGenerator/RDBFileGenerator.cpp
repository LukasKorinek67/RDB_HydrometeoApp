#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>
#include <tchar.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>


int random(int , int );
char *randstring(int length);
char* getfield(char* line, int num);

int main(int argc, char* argv[]){

	int no_names = 5;
	char *name[6] = { "Karel", "Petr", "Zuzana", "Kamila", "Anezka", "Jan" };

	int no_surenames = 5;
	char *surename[6] = { "Novak", "Smrz", "Nova", "Nejedla", "Ceska", "Zizka" };

	int no_emails = 5;
	char *email[6] = { "karel.novak@abc.com", "petr1@emial.com", "zuzana.nova@abc.com", "kamila.ceska@abc.com", "anezka.nejedla@eltrom.cz", "jan.zizka@eltrom.cz" };
	
	int no_depts = 3;
	char *dep[4] = { "Abc", "Aka", "ABC", "eltrom"};

	int no_adrs = 3;
	char *adr[4] = { "Sladka", "Nova", "Uzka", "Sirkova" };

	int no_adr_nums = 3;
	char *adrnum[4] = { "23", "2", "545/1", "24" };

	int no_adr_cities = 3;
	char *adrcity[4] = { "Liberec", "Praha", "Plzen", "Brno" };

	int no_phones = 6;
	char *phone[7] = { "+420777458547", "+420535161254", "+4206302541542", "+420777985632","+420602458745", "+420772698452", "+420775632874" };


	int no_devices = 2;
	char *device[3] = { "Dev01", "Measure 1000", "tempX1" };
	char *deltas[3] = { "0.1", "1", "0.01" };
	char *manufacturer[3] = { "XXX", "kdoVI", "Ta12" };
	char *inv[3] = { "INV-2354", "CZ1254", "AX547" };
	char *voltage[3] = { "[12]", "[12,24]", "[12,24,110,230]" };

	FILE* stream = fopen("input.txt", "r");
	if (stream == NULL) {
		printf("No input.txt provided in working forlder.");
		return 100;
	}
	char* tmp = NULL;
	char *place = "Liberec";
	char * sfrom = NULL;
	char * sto = NULL;

	char line[1024];
	fgets(line, 1024, stream);
	tmp = _strdup(line);
	place = getfield(tmp, 1);
	tmp = _strdup(line);
	sfrom = getfield(tmp, 2);
	tmp = _strdup(line);
	sto = getfield(tmp, 3);

	if (place !=NULL && sfrom != NULL && sto != NULL) {
		time_t t;
		srand((unsigned)time(&t));
		long from = 0;
		long to = 0;
		from = atol(sfrom);
		to = atol(sto);


		char *filename = (char *)malloc(400 * sizeof(char));
		strcpy(filename, place);



		float temp = 0;
		float pressure = 1000;
		int rain = 0;
		int plus = 0;
		float delta = 0;

		int rand = 0;
		int rand2 = 0;

		char *filename_json = (char *)malloc(400 * sizeof(char));
		strcpy(filename_json, filename);

		strcat(filename_json, ".json");
		FILE *f_json = fopen(filename_json, "w");

		if ( f_json == NULL ){
			printf("Error while creating output files!\n");
			exit(1);
		}

		fprintf(f_json, "%s", "{\n");
		fprintf(f_json, "\t\"place\":\"%s\",\n",  place);
		fprintf(f_json, "\t\t%s", "\"type\": {\n");
		int manual = random(0, 1);

		if (manual == 1) {
			printf("Manual Measurement...\n");
			rand = random(0, no_names);
			fprintf(f_json, "\t\t\t\"manual\": {\n");
			fprintf(f_json, "\t\t\t\"name\": \"%s\",\n", name[rand]);
			fprintf(f_json, "\t\t\t\"surename\": \"%s\",\n", surename[rand]);
			fprintf(f_json, "\t\t\t\"email\": \"%s\",\n", email[rand]);
			rand = random(0, no_depts);
			fprintf(f_json, "\t\t\t\"deptitle\": \"%s\",\n", dep[rand]);
			rand2 = random(0, no_phones);
			fprintf(f_json, "\t\t\t\"depphone\": \"%s\",\n", phone[rand2]);
			fprintf(f_json, "\t\t\t\"depaddress\": [\"%s\",\"%s\",\"%s\"],\n", adr[rand], adrnum[rand], adrcity[rand]);
		}else {
			printf("Auto Measurement...\n");
			rand = random(0, no_devices);
			fprintf(f_json, "\t\t\t\"auto\": {\n");
			fprintf(f_json, "\t\t\t\"title\": \"%s\",\n", device[rand]);
			fprintf(f_json, "\t\t\t\"delta\": \"%s\",\n", deltas[rand]);
			fprintf(f_json, "\t\t\t\"manufacturer\": \"%s\",\n", manufacturer[rand]);
			fprintf(f_json, "\t\t\t\"voltage\": %s,\n", voltage[rand]);
			fprintf(f_json, "\t\t\t\"regnum\": \"%s\",\n", inv[rand]);
		}

		fprintf(f_json, "%s", "\t\t\t\"values\":[\n");

		while (from < to) {
			plus = random(0, 1);
			delta = ((float)(random(0, 10))) / 10;
			if (plus == 1) {
				temp = temp + delta;
			}
			else {
				temp = temp - delta;
			}

			plus = random(0, 1);
			delta = ((float)(random(0, 100))) / 10;
			if (plus == 1 && pressure < 1084) {
				pressure = pressure + delta;
			}
			else {
				pressure = pressure - delta;
			}
			if (plus == 0 && pressure > 870) {
				pressure = pressure - delta;
			}
			else {
				pressure = pressure + delta;
			}

			plus = random(0, 1);
			delta = (random(0, 100)) / 10;
			if (plus == 0 && (rain - delta) > 0) {
				rain = rain - delta;
			}
			else {
				rain = rain + delta;
			}

			printf("%ld, ", from, to);
			if ((from + 60) >= to) {
				fprintf(f_json, "\t\t\t\t[%ld, %.1f, %.1f, %d ]\n", from, temp, pressure, rain);
			}
			else {
				fprintf(f_json, "\t\t\t\t[%ld, %.1f, %.1f, %d ],\n", from, temp, pressure, rain);
			}
			from+=60;
		}
		fprintf(f_json, "			]\n");
		fprintf(f_json, "		}\n");
		fprintf(f_json, "	}\n");
		fprintf(f_json, "}\n");
		fclose(f_json);

		return 1;
	}else{
		printf("Error parsing input.txt, expected place,timestamp_from,timestamp_to");
		return 10;
	}

	return 0;
}

char* getfield(char* line, int num) {
	char *tok;
	for (tok = strtok(line, ",");
		tok && *tok;
		tok = strtok(NULL, ",\n"))
	{
		if (!--num)
			return tok;
	}
	return NULL;
}

int random(int min, int max){
	return (rand() % (max + 1 - min)) + min;
}