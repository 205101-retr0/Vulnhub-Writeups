This is a boot-to-root machine so there will be no flag.

After a nmap scan we get that there is only 2 ports 22/ssh and 80/http.

Running gobuster on website gave us nothing. But in the source code we see a comment saying ROT47.

On the webpage we can see one if the entries not making any sense so we can decode this using [ROT47 decoder](https://cryptii.com/pipes/rot13-decoder) to see if we makes any sense. And bingo! we might have potential credentials to ssh login.

```D92:=6?5C2	4J36CDA=@:E --> shailendra	cybersploit1```

We ssh into the server using these credentials. ___User: shailendra, Password: cybersploit1___.

In the server we see a file called hint.txt which contains only one word docker.

So we may be able to get root using docker setuid. We can copy the command from [GTFObins docker](https://gtfobins.github.io/gtfobins/docker/) under the SUID section.

And there we have the root access. 