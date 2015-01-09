use Crypt::RSA::ES::OAEP;

my $oaep = new Crypt::RSA::ES::OAEP; 

    my $ct = $oaep->encrypt( Key => $key, Message => $message ) || 
                die $oaep->errstr; 

    my $pt = $oaep->decrypt( Key => $key, Cyphertext => $ct )   || 
                die $oaep->errstr; 