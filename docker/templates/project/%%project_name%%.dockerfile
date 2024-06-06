FROM scratch

ARG CONFIGURATION=prod

ADD root /
ADD configurations/$CONFIGURATION/root /