#!/usr/bin/perl -w
my $line_number = 0;
while (<>) {
	chomp;
	my @fields = split /\s+/;
	if($line_number%15==0) {
		print $fields[3]."\t";
	}
	print $fields[5];
	if($line_number%15==14) {
		print "\n";
	} else {
		print "\t";
	}
	$line_number++;
}
